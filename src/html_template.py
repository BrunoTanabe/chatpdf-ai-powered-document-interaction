# html_template.py: Script para criar os templates de HTML para a interface do chatbot Aila

hide_st_style = '''
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
'''

css = '''
    <style>
        .chat-message {
            padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
        }

        .chat-message.user {
            background-color: #C7000F;
            justify-content: flex-start;
            flex-direction: row-reverse;
        }

        .chat-message.bot {
            background-color: #C70039;
            justify-content: flex-start;
            flex-direction: row;
        }

        .chat-message .avatar {
            width: 20%;
            display: flex;
            margin-right: auto;
            margin-left: auto;
        }

        .chat-message .avatar img {
            max-width: 86px;
            max-height: 86px;
            border-radius: 50%;
            object-fit: cover;
            display: flex;
            margin-right: auto;
            margin-left: auto;
        }

        .chat-message.bot .message {
            width: 80%;
            padding: 0 1.5rem 0 1.5rem;
            color: #fff;
            text-align: left;
        }

        .chat-message.user .message {
            width: 80%;
            padding: 0 1.5rem 0 1.5rem;
            color: #fff;
            text-align: left;
        }
    </style>
'''

ai_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="./app/static/ai_profile_photo.png">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

human_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="./app/static/human_profile_photo.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''