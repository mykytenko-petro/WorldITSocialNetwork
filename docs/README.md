# WorldIT Social Network

[Українська версія](#worldit-social-network-українська)

### Goal of the project
WorldIT Social Network is a Django-based social platform that brings together core social networking features such as user profiles, posts, notifications, and real-time messaging. The project is designed to provide a modern web experience with both traditional web views and real-time chat capabilities using Django Channels.

A notable aspect of this project is that the frontend was adapted to work with a JavaScript-based backend for WebSocket communication. This approach made real-time messaging possible through a separate socket server and showed that building a scalable and reliable WebSocket infrastructure is a non-trivial task.

### Team members
- [Mykytenko Petro (team lead)](https://github.com/mykytenko-petro)
- [Luchaninova Tania](https://github.com/TaniaLuchaninova)
- [Skulskuia Andrii](https://github.com/andrewskulskuia)
- [Chornorot Andriy](https://github.com/ChornorotAndriy)
- [Ezhova Eva](https://github.com/EvaEzhova)
- [Kyrychenko Daniil](https://github.com/DaniilKyrychenko)

### Navigation
- [Goal of the project](#goal-of-the-project)
- [Team members](#team-members)
- [Main dependencies used](#main-dependencies-used)
- [How to launch the project](#how-to-launch-the-project)
- [Conclusion](#conclusion)

### Main dependencies used
This project relies on the following main technologies and packages:
- Django 4.2 for the web application framework
- Channels and Daphne for real-time WebSocket communication
- Pillow for image handling
- django-debug-toolbar for development debugging
- python-dotenv for environment configuration
- Cloudinary storage for media uploads
- psycopg2-binary and sshtunnel for optional database connectivity

### How to launch the project
This project is intended to run with Python 3.13.

1. Clone the repository:
   ```bash
   git clone https://github.com/mykytenko-petro/WorldITSocialNetwork.git
   ```
2. Move into the project folder:
   ```bash
   cd WorldITSocialNetwork
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Move to the Django project directory:
   ```bash
   cd WorldITSocialNetwork
   ```
6. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
7. Start the development server:
   ```bash
   python manage.py runserver
   ```

If needed, configure the required environment variables for database, email, and Cloudinary settings before launching the project.

### Content
This project is organized into several Django apps, each responsible for a specific part of the social network experience.

- **chat_app** — handles private and group messaging, chat views, and real-time communication.
![]()
- **home_app** — provides the landing page and profile completion flow.
![]()
- **notification_app** — manages notifications and event-driven updates.
![]()
- **post_app** — supports creating, displaying, and managing posts and related media.
![]()
- **profile_app** — handles user profile pages and profile-related information.
![]()
- **user_app** — manages authentication, user accounts, and user-specific logic.
![]()

### Conclusion
This project was a valuable experience for the team because it combined backend development, real-time communication, and UI integration in a single full-stack product. It helped us improve our understanding of Django architecture, WebSocket-based features, and the challenges of connecting different services in a modern social platform.

During development, the team encountered several difficulties, especially around integrating real-time messaging, adapting the frontend to a JavaScript-based socket backend, and maintaining a reliable structure for user data, media, and notifications. These challenges made the project more realistic and taught us how to solve integration problems step by step.

In the future, this project can be expanded by adding stronger moderation tools, better notification systems, improved performance, and more advanced chat features. To keep it maintainable, the team should continue refining the architecture, documenting the API and socket flow, and regularly reviewing code quality and deployment readiness.

---

# WorldIT Social Network (Українська)

### Мета проєкту
WorldIT Social Network — це соціальна платформа на Django, яка об’єднує основні функції соцмереж: профілі користувачів, пости, сповіщення та чат у реальному часі. Проєкт розроблено як сучасний веб-додаток із традиційними веб-сторінками та функціями реального часу за допомогою Django Channels.

Особливістю цього проєкту є те, що фронтенд було адаптовано для роботи з JavaScript-бекендом для WebSocket-з’єднань. Це дозволило реалізувати реальний чат через окремий сокет-сервер і показало, що створення масштабованої та надійної WebSocket-архітектури — непросте завдання.

### Команда
- [Микитенко Петро (тімлід)](https://github.com/mykytenko-petro)
- [Лучанінова Тетяна](https://github.com/TaniaLuchaninova)
- [Скульськй Андрій](https://github.com/andrewskulskuia)
- [Чорнорот Андрій](https://github.com/ChornorotAndriy)
- [Єжова Єва](https://github.com/EvaEzhova)
- [Кириченко Даніїл](https://github.com/DaniilKyrychenko)

### Навігація
- [Мета проєкту](#мета-проєкту)
- [Команда](#команда)
- [Основні залежності](#основні-залежності)
- [Як запустити проєкт](#як-запустити-проєкт)
- [Вміст](#вміст)
- [Висновок](#висновок)

### Основні залежності
Проєкт використовує такі основні технології та пакети:
- Django 4.2 як веб-фреймворк
- Channels та Daphne для WebSocket-зв’язку в реальному часі
- Pillow для роботи з зображеннями
- django-debug-toolbar для налагодження під час розробки
- python-dotenv для роботи з налаштуваннями середовища
- Cloudinary Storage для зберігання медіа-файлів
- psycopg2-binary та sshtunnel для додаткової підключення до баз даних

### Як запустити проєкт
Цей проєкт розрахований на Python 3.13.

1. Клонуйте репозиторій:
   ```bash
   git clone https://github.com/mykytenko-petro/WorldITSocialNetwork.git
   ```
2. Перейдіть у папку проєкту:
   ```bash
   cd WorldITSocialNetwork
   ```
3. Створіть і активуйте віртуальне середовище:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
4. Встановіть залежності:
   ```bash
   pip install -r requirements.txt
   ```
5. Перейдіть у каталог Django-проєкту:
   ```bash
   cd WorldITSocialNetwork
   ```
6. Застосуйте міграції бази даних:
   ```bash
   python manage.py migrate
   ```
7. Запустіть сервер розробки:
   ```bash
   python manage.py runserver
   ```

Якщо потрібно, перед запуском налаштуйте змінні середовища для бази даних, електронної пошти та Cloudinary.

### Вміст
Проєкт організовано у кілька Django-додатків, кожен із яких відповідає за певну частину функціоналу соціальної мережі.

- **chat_app** — відповідає за приватні та групові чати, перегляд чатів і комунікацію в реальному часі.
  ![]()
- **home_app** — забезпечує головну сторінку та процес заповнення профілю.
  ![]()
- **notification_app** — керує сповіщеннями та подіями, що оновлюються в реальному часі.
  ![]()
- **post_app** — підтримує створення, показ і управління постами та медіафайлами.
  ![]()
- **profile_app** — відповідає за сторінки профілів користувачів і пов’язану з ними інформацію.
  ![]()
- **user_app** — керує автентифікацією, обліковими записами користувачів та пов’язаною логікою.
  ![]()

### Висновок
Цей проєкт став корисним для команди, бо поєднав розробку бекенду, реальний час і інтеграцію інтерфейсу в єдиний продукт. Він допоміг краще зрозуміти архітектуру Django, функції на основі WebSocket і труднощі з’єднання різних сервісів у сучасній соціальній платформі.

У процесі розробки команда зіткнулася з кількома труднощами, особливо під час інтеграції чату в реальному часі, адаптації фронтенду до JavaScript-бекенду для сокетів і підтримки надійної структури для даних користувачів, медіа та сповіщень. Ці виклики зробили проєкт більш реалістичним і допомогли навчитись розв’язувати інтеграційні проблеми крок за кроком.

У майбутньому цей проєкт можна розширити шляхом додавання більш потужних інструментів модерації, кращих систем сповіщень, покращення продуктивності та більш просунутих функцій чату. Для підтримки проєкту в хорошому стані команді варто продовжувати покращувати архітектуру, документувати API та потік сокетів, а також регулярно перевіряти якість коду й готовність до розгортання.
