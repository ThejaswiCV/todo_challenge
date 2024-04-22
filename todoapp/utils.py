import requests
from django.conf import settings
import os

GITHUB_PERSONAL_ACCESS_TOKEN = os.environ.get('GITHUB_PERSONAL_ACCESS_TOKEN')


def generate_project_summary(project):
    # Project Title
    markdown_content = f"# {project.title}\n\n"

    #  Completed Todos / Total Todos
    completed_todos_count = project.todos.filter(status='completed').count()
    total_todos_count = project.todos.count()
    markdown_content += f"Summary: {completed_todos_count} / {total_todos_count} completed\n\n"

    #  Pending Todos
    markdown_content += "## Pending Todos\n"
    pending_todos = project.todos.filter(status='pending')
    for todo in pending_todos:
        markdown_content += f" [ ] {todo.name}\n\n"

    #  Completed Todos
    markdown_content += "\n## Completed Todos\n"
    completed_todos = project.todos.filter(status='completed')
    for todo in completed_todos:
        markdown_content += f" [x] {todo.name}\n"

    return markdown_content




def create_secret_gist(project_name,markdown_content):
    
    url = 'https://api.github.com/gists'

   
    payload = {
        'description': 'Project Summary',
        'public': False,
        'files': {
            'summary.md': {
                'content': markdown_content
            }
        }
    }

    
    headers = {
        
        'Authorization': f'token {GITHUB_PERSONAL_ACCESS_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }

   
    response = requests.post(url, json=payload, headers=headers)
    
    
    if response.status_code == 201:
        gist_url = response.json()['html_url']
        
        
        file_path = os.path.join(settings.MEDIA_ROOT, f'{project_name}.md')
        with open(file_path, 'w') as file:
            file.write(markdown_content)
        
        return gist_url, file_path
    else:
        return None, None
