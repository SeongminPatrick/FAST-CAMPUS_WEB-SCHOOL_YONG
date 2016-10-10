#개발 환경 세팅

#### pyenv설치

- https://github.com/yyuu/pyenv-installer
- 위의 링크로 들어가 pyenv를 설치한다.
- 자동 실행을 위해 .bash_profile에 필요한 명령어를 복사 한다.

		export PATH="~/.pyenv/bin:$PATH"
		eval "$(pyenv init -)"
		eval "$(pyenv virtualenv-init -)"
		
		

####  파이썬 설치
pyenv install 3.4.3

#### 가상환경 생성
- pyenv 3.4.3 fc-virenv
- 원하는 파이썬 버젼과 가상환경 이름을 지정한다.

#### local에 가상환경 지정
- local fc-virenv
- 가상환경이 자동 실행될 수 있도록 폴더를 지정한다.

#### 장고설치 및 프로젝트 생성
- pip install django
- django-admin startproject project_name
- python manage.py startapp app_name

####  interpreter 설정
- file -> settings-> project-> Interprenter에서 가상머신을 선택해 준다.
