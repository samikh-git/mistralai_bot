<h1> Mistral AI Reddit Bot </h1>

<p> This is primarily an educational project on my end to try and understand the Reddit API and how to build Reddit bots. I wanted to try to create a Reddit bot that could answer some basic questions using LLMs. I settled on Mistral AI as it has a good free usage and is very quick. It also provides relatively decent answers. </p>

<p> To use these bots, you simply need to run the <code>bot.py</code> file and call the <code>main</code> function. This should then run the bot until it finds the first post to reply to. It will ask if you wish to proceed and find another post for which you want it to answer.</p>

<p>Here is a rundown of the execution of the Reddit bot.</p>
<pre><code class="language-bash">
    python bot.py
        >>> main(subreddit="AskReddit")
        "Sample answer"
        Do you wish to procced? [yes]/[no] no
        FINISHED
</code></pre>

<p> If you want to use this on your own, you will need to create your own Reddit APP and have your own Mistral API key. You will also need to install some dependencies. Using PIP, you only need to run <code>pip install praw mistralai</code>. Here is a link to the process to creating a Reddit APP <a>https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps</a>  and to the Mistral dashboard <a>https://console.mistral.ai/home</a>. Here  is also a link to the PRAW tutorial that I used to make the app: <a>https://praw.readthedocs.io/en/latest/tutorials/reply_bot.html</a>. </p>
