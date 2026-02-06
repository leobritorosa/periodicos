import csv
from django.core.management.base import BaseCommand
from periodico.models import Professor  # Substitua 'your_app' pelo nome do seu app
import re
class Command(BaseCommand):
    help = 'Atualizando docenetes dados de docentes do arquivo CSV'

    def handle(self, *args, **options):
        file_path = '/home/leonardo/Nova pasta/BANCO_METRICAS_1_final2.csv'
        
        with open(file_path, 'r', encoding='utf-8') as f:
            # O arquivo usa ';' como delimitador
            reader = csv.DictReader(f, delimiter=';')
            
          
            
            for row in reader:
                # Limpeza simples de possíveis espaços em branco
               
                id= re.sub(r'\D', '', row['\ufeffId'].strip())
                if id :
                    professor=Professor.objects.filter(id=id)
                    if professor:
                        professor=professor.first()
                        professor.area=row['area']
                        professor.grande_area=row['grandearea']
                        professor.aceitos=row['aceitos']
                        professor.capitulos=row['capitulos']
                        professor.congresso=row['congresso']
                        professor.livros=row['livros']
                        professor.periodico=row['periodico']
                        professor.producao_biblio=row['producao_bibilo']
                        professor.resumos=row['resumos']
                        professor.save()
                        
                
                            
        self.stdout.write(self.style.SUCCESS(f'Sucesso: professores importados.'))