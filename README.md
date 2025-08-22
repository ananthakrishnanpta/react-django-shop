# Shopping Site with React + Django


## Setup

***Clone this repository***

```bash
    git clone <repo-link>
```

1. Setup the python virtual environment

    ```
    Ensure that python version >= 3.11 is installed on your computer.
    >> python --version
    ```

    Run:
    ```bash
    cd <repo_folder>
    python -m venv virt
    ```
2. Activate the virtual environment
    
    i. Windows Systems
    ```bash
    virt/Scripts/activate
    ```
    ii. UNIX Systems (MAC/Linux)
    ```bash
    source virt/bin/activate
    ```
3. Install python dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Migrate Schema 
**cd into `backend` folder`**
    ```cd backend```
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5. Create Superuser account for accessing django admin panel
    ```bash
    python manage.py createsuperuser
    ```
    - Follow the instructions
    
6. Run the backend server
    ```bash
    python manage.py runserver <port_number>
    ```