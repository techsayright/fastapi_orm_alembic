# fastapi_orm_alembic

python3 -m venv <virtual_env_name>
source virtual_env_name/bin/activate
pip install -r requirements.txt


#for alembic setup
if you have created then dont do below 1 step(in my case its done)
alembic init <alembic_folder_name>

#When you change something on models.py file either add table/column or update/delete table/column, follow below steps to make reflect of that in database:

->alembic revision --autogenerate -m "msg" #it will create revision whatever the changes will be there on models.py in compare of current database #so check python file added on alembic->version, and after reviewing make changes accordingly

->alembic upgrade head
