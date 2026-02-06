import csv
from django.core.management.base import BaseCommand
from periodico.models import Professor  # Substitua 'your_app' pelo nome do seu app

class Command(BaseCommand):
    help = 'Importa dados de docentes do arquivo CSV'

    def handle(self, *args, **options):
        file_path = 'DADOS_DOCENTES_IFMA_MONTE_CASTELO.csv'
        
        with open(file_path, 'r', encoding='utf-8') as f:
            # O arquivo usa ';' como delimitador
            reader = csv.DictReader(f, delimiter=';')
            
            professores_para_criar = []
            for row in reader:
                # Limpeza simples de possíveis espaços em branco
                nome = row['Nome_CV'].strip()
                email = row['E-mail'].strip()
                
                # Cria o objeto na memória
                professores_para_criar.append(
                    Professor(
                        id=row['Id'],
                        nome_cv=nome,
                        email=email
                    )
                )
            
            # Inserção em lote (mais performático)
            Professor.objects.bulk_create(professores_para_criar, ignore_conflicts=True)
            
        self.stdout.write(self.style.SUCCESS(f'Sucesso: {len(professores_para_criar)} professores importados.'))