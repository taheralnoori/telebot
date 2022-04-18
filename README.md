Python Telepot Inline Sample bot
====

Sample inline bot based on [telepot API](https://github.com/nickoala/telepot).

Run on heroku
----
Create an app on your repository folder:

```bash
$ heroku create
Creating app... done, stack is cedar-14
https://hidden-sea-76399.herokuapp.com/ | https://git.heroku.com/hidden-sea-76399.git

```

As you have to use your token at bot's command run you can:

Add at _Procfile_ with command statement:
```
worker: python inline_sample.py TOKEN
```

Or replace previous statement with shown above:
```
worker: python inline_sample.py $TOKEN
```

And configure your **TOKEN** as a config var:

```bash
$ heroku config:set TOKEN=<TOKEN>
Setting config vars and restarting hidden-sea-76399... done
TOKEN: <TOKEN>
```

Deploy your code to heroku:

```bash
$ git push heroku master
Counting objects: 9, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (6/6), done.
Writing objects: 100% (9/9), 2.76 KiB | 0 bytes/s, done.
Total 9 (delta 0), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> Python app detected
remote: -----> Installing python-2.7.11
remote:      $ pip install -r requirements.txt
remote:        Collecting telepot (from -r requirements.txt (line 1))
remote:          Downloading telepot-6.6.zip (44kB)
remote:        Collecting requests>=2.4.0 (from telepot->-r requirements.txt (line 1))
remote:          Downloading requests-2.9.1-py2.py3-none-any.whl (501kB)
remote:        Installing collected packages: requests, telepot
remote:          Running setup.py install for telepot: started
remote:            Running setup.py install for telepot: finished with status 'done'
remote:        Successfully installed requests-2.9.1 telepot-6.6
remote:
remote: -----> Discovering process types
remote:        Procfile declares types -> worker
remote:
remote: -----> Compressing...
remote:        Done: 33.3M
remote: -----> Launching...
remote:        Released v4
remote:        https://hidden-sea-76399.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy.... done.
To https://git.heroku.com/hidden-sea-76399.git
 * [new branch]      master -> master
```

Scale your heroku host so it can start `workers`:

```bash
$ heroku ps:scale worker=1
```

To show your host logs:
```bash
$ heroku logs --tail
```

References
----

### [Telepot](https://github.com/nickoala/telepot/blob/master/REFERENCE.md)

### [Telegram Bot API](https://core.telegram.org/bots/api)

### [Heroku - Getting started with python](https://devcenter.heroku.com/articles/getting-started-with-python)
