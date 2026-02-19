import csv, re
from django.core.management.base import BaseCommand
from periodico.models import Professor,Publicacao  # Substitua 'your_app' pelo nome do seu app

class Command(BaseCommand):
    help = 'Importa dados de docentes do arquivo CSV'

    def handle(self, *args, **options):
        file_path = '/home/leonardo/BANCO_PRODUCAO_BIBLIOGRAFICA.csv'
        publicacoes_para_criar=[]
        with open(file_path, 'r', encoding='utf-8') as f:
            # O arquivo usa ';' como delimitador
            reader = csv.DictReader(f, delimiter=';')
            print(f"Os cabeçalhos encontrados são: {reader.fieldnames}")
           
            for row in reader:
                id= re.sub(r'\D', '', row['\ufeffId'].strip())
                professor=Professor.objects.filter(pk=id)
                
                if professor:
                    professornovo=professor.first()
            
                    if row['Producao']:
                        publicacoes_para_criar.append(
                            Publicacao (professor_id=professornovo.pk,
                                        titulo=row['Producao'],
                                        link=row['Link'],
                                            )
                            )
                        print(professornovo)
                        
                        # # Inserção em lote (mais performático)
            Publicacao.objects.bulk_create(publicacoes_para_criar, ignore_conflicts=True)
            
                
        self.stdout.write(self.style.SUCCESS(f'Sucesso: {len(publicacoes_para_criar)} professores importados.'))