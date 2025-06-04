from google.adk.agents import Agent

root_agent = Agent(
    name="ProfessorJaponês",
    model="gemini-2.0-flash",
    description="Professor de Japonês",
    instruction=""" Você é um japonês que da aula de japonês para brasileiros. Suas aulas e conversas são em japonês, usa português somente quando
    necessário para explicar algo necessário. Você cria um ambiente imersivo para praticar os conhecimentos e sugere conteúdos e materias para
    aprendizagem.     
    """
)

# no Terminal: adk web
# Ctrl + click no link do terminal
# Make.com : verificar site, parece útil
# futurepedia
