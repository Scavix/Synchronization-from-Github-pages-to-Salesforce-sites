# Salesforce-Rest-Api-Updater

## What is that?
Synchronization flow between a webpage (used to collect links, hosted on github pages) to Salesforce.

<p align="center">
  <img src="https://github.com/Scavix/Salesforce-Rest-Api-Updater/blob/main/mySF.drawio.svg" />
</p>

## Actors
<ul>
  <li>Github for version control</li>
  <li>Github pages as webpage (duh)</li>
  <li>Heroku as script hosting (python script)</li>
  <li>Salesforce as CRM</li>
  <li>Salesforce sites as website (double duh)</li>
</ul>

## What happens?
<ul>
  <li>Every 24 hours a python script hosted on heroku (scheduled through Herouku scheduler) send a GET REST API request to my github page</li>
  <li>Through the beautifulsoup library and some regexs the page is parsed</li>
  <li>A JSON is prepared and sent to Salesforce standard APIs URL</li>
</ul>
