import os

models = [
    'professor', 'disciplinas', 'tempo', 'aula', 'turma', 
    'diasemana', 'semestre', 'predio', 'sala'
]

base_dir = r'd:\Code\ProjetosIF\GestorDoTempo\GestorDoTempo\templates\cadastro'

if not os.path.exists(base_dir):
    os.makedirs(base_dir)

for model in models:
    # List Template
    list_content = f"""{{% extends 'cadastro/base.html' %}}

{{% block content %}}
<div class="card mt-4">
    <div class="card-header d-flex justify-content-between align-items-center">
        <h2 class="mb-0">Lista de {model.capitalize()}</h2>
        <a href="{{% url '{model}_create' %}}" class="btn btn-light text-success fw-bold">Novo {model.capitalize()}</a>
    </div>
    <div class="card-body">
        <div class="table-responsive">
            <table class="table table-hover">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Descrição</th>
                        <th>Ações</th>
                    </tr>
                </thead>
                <tbody>
                    {{% for item in object_list %}}
                    <tr>
                        <td>{{{{ item.id }}}}</td>
                        <td>{{{{ item }}}}</td>
                        <td>
                            <a href="{{% url '{model}_update' item.pk %}}" class="btn btn-sm btn-primary">Editar</a>
                            <a href="{{% url '{model}_delete' item.pk %}}" class="btn btn-sm btn-danger">Excluir</a>
                        </td>
                    </tr>
                    {{% empty %}}
                    <tr>
                        <td colspan="3" class="text-center">Nenhum registro encontrado.</td>
                    </tr>
                    {{% endfor %}}
                </tbody>
            </table>
        </div>
    </div>
</div>
{{% endblock %}}
"""
    with open(os.path.join(base_dir, f'{model}_list.html'), 'w', encoding='utf-8') as f:
        f.write(list_content)

    # Form Template
    form_content = f"""{{% extends 'cadastro/base.html' %}}

{{% block content %}}
<div class="row justify-content-center mt-4">
    <div class="col-md-8">
        <div class="card">
            <div class="card-header">
                <h2 class="mb-0">{{{{ view.action }}}} {model.capitalize()}</h2>
            </div>
            <div class="card-body">
                <form method="post">
                    {{% csrf_token %}}
                    {{{{ form.as_p }}}}
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                        <a href="{{% url '{model}_list' %}}" class="btn btn-secondary me-md-2">Cancelar</a>
                        <button type="submit" class="btn btn-primary">Salvar</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{{% endblock %}}
"""
    with open(os.path.join(base_dir, f'{model}_form.html'), 'w', encoding='utf-8') as f:
        f.write(form_content)

    # Confirm Delete Template
    delete_content = f"""{{% extends 'cadastro/base.html' %}}

{{% block content %}}
<div class="row justify-content-center mt-4">
    <div class="col-md-6">
        <div class="card border-danger">
            <div class="card-header bg-danger text-white">
                <h2 class="mb-0">Excluir {model.capitalize()}</h2>
            </div>
            <div class="card-body">
                <p class="lead">Tem certeza que deseja excluir "{{{{ object }}}}"?</p>
                <form method="post">
                    {{% csrf_token %}}
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                        <a href="{{% url '{model}_list' %}}" class="btn btn-secondary me-md-2">Cancelar</a>
                        <button type="submit" class="btn btn-danger">Confirmar Exclusão</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{{% endblock %}}
"""
    with open(os.path.join(base_dir, f'{model}_confirm_delete.html'), 'w', encoding='utf-8') as f:
        f.write(delete_content)

print("Templates created successfully.")
