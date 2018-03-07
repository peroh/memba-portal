# Portsea Member Management App

When I was Education Director at my lifesaving club, I noticed that managing
all of the members, their awards, and the paperwork was very difficult. I've
always been interested in working on projects that have a use-case, so I
started building this membership management tool.

## Features

* Manage database of members
* Manage courses and events
* Manage member awards
* Automate paperwork creation and completion for courses

## Functionality

* Seperate apps for Members, Courses, Awards, Events, and PDF Generation
* Mix of class/function based views
* Custom `User` model to signup and uses standard django auth with
  an email address
* Basic bootstrap templates


## Installing and Running

* Create a virtualenv running Python 2.7
* `pip install -r requirements.txt`
* `python manage.py migrate`
* `python manage.py runserver`

With no data loaded in, the functionality is very limited. There is some
necessary data to create from the admin panel before being useful, such as
`EventType`s and `CourseType`s. To adminstrate these:

* `python manage.py createsuperuser`
* Enter email, name and password
* Visit `/admin` and log in

## Next Steps

When I get some free time I'd love to finish off the functionality, make it look
pretty, deploy and roll out with some other lifesaving clubs to help them as
well.
