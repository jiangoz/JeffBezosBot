# JeffBezosBot

Jeff Bezos bot for Amazon Discord server

![Bezos](https://i.imgur.com/TzGMQd0.png)
![Customer Obsession](https://i.imgur.com/RhMdrl6.png)

## Local Development
1) Create virtual environment in bot directory: `py -m venv bot_env`
2) Activate virtual environment on Linux: `source bot_env/bin/activate` or Windows: `bot_env\Scripts\activate`
3) Windows - change execution policy for PowerShell (if running above script is disabled): `Set-ExecutionPolicy -Scope "CurrentUser" -ExecutionPolicy "RemoteSigned"`
4) Install requirements/dependencies: `pip install -r requirements.txt`

## CI/CD Setup using Github Actions
0) Setup for VPS
   1) [Get a VPS](https://aws.amazon.com/pm/ec2/?trk=36c6da98-7b20-48fa-8225-4784bced9843&sc_channel=ps&sc_campaign=acquisition&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Compute|EC2|US|EN|Text&s_kwcid=AL!4422!3!488982705723!e!!g!!aws%20free%20ec2&ef_id=Cj0KCQjwyYKUBhDJARIsAMj9lkEK6oOMduDFrTVEJzqBeOe-eIe5tpIJ-La_0rkax5nCMn1swQ2NGSwaAtt8EALw_wcB:G:s&s_kwcid=AL!4422!3!488982705723!e!!g!!aws%20free%20ec2)
   2) [Install docker](https://docs.docker.com/engine/install/)
   3) Create ~/jeffbezo-bot directory
        ```
        mkdir ~/jeffbezo-bot
        ```
   4) Create ~/jeffbezo-bot/.env file
        ```
        touch ~/jeffbezo-bot/.env
        ```
      1) put bot token inside (ex TOKEN=my token here)
      2) Any other environment variables necessary. Sample .env file:
        ```
        TOKEN=<my bot token here>
        PREFIX=<my prefix here>
        ```
1) Create GitHub Action secrets for deploying to VPS
   1) USERNAME (username to ssh into vps)
   2) HOST
   3) PORT (default is 22)
   4) SSH_KEY (private key to ssh into vps)
2) Run GitHub actions :)
### Useful References/Links:
- **discord.py Documentation:** https://discordpy.readthedocs.io/en/latest/index.html  
- **Official Discord API:** https://discordapp.com/developers/docs/intro  
- **Python3 Documentation:** https://docs.python.org/3/
