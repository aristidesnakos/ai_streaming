import os
from dotenv import load_dotenv
import tempfile

load_dotenv()

ENV = os.getenv("ENV")
STAGE = os.getenv("STAGE")

convo_starter_question = "Ask a simple question regarding ONE of my topics of interest, in my practice language. Just output the question itself."
lesson_starter = "Let's have a lesson."
onboarding_conclusion = "That was a fun onboarding experience! What's next?"
onboard_fb_template = {"English":"HXc8ac89048cc05eaef621ac2c0586c6d2",
                       "Japanese":"HXbde4a4945ae0a8fe122d16c5585a5b77", 
                       "Spanish":"HX322ac8ccec4b86ff7ad27dfab8e4eee0"}

gen_ai_image_phrases = [
    "I painted a picture with your top 5 words for you.",
    "Every picture tells a story. This is a story made with your top 5 words.",
    "A picture is worth a thousand words, so here are your top 5 words.",
    "I show, I don't tell, your top 5 words."
]

ERROR_MESSAGES = [
    "I am sorry 😵‍💫, it seems I am having trouble functioning today.",
    "I am sorry 🫠, I am not able to process your request at the moment."
]

LESS_WORDS_MESSAGES = [
    "Your message is a bit lengthy 😊. Could you please summarize it in fewer words?",
    "🥴 Looks like your message exceeded our character limit. Can you make it a tad shorter?",
    "We love reading your thoughts! 🤪 But could you condense them a bit for us?",
    "That's quite detailed! 🐰 Can you rephrase in a shorter message?",
    "Your enthusiasm is contagious! 😉 Mind keeping it brief for a quick read?",
    "We're all ears! 👂 Please make your message more compact for us.",
    "A bit too long for our chat box 😅. How about a shorter version?"
]

PLEASE_USE_MIC_MESSAGES = [
    "Oops, that didn't quite make sense to me. Could you please repeat that using the mic? 🎙️",
    "My apologies, I'm having trouble understanding. Mind trying again with the ,microphone?  🎙️",
    "Hmm, I didn't catch that. Could you give it another go through the mic?"]

TEXT_AUDIO_ONLY_MESSAGES = [
    "Feel free to drop a message or voice note 📝🎙️.",
    "Send us a text or an audio clip, your choice! ✉️🔊",
    "Text messages or voice messages welcome here! 📲🎤",
]

ALT_CORRECTION_MESSAGES = [
    "Returning a grammatically correct version of your sentence that sounds natural.",
    "Providing a natural-sounding, grammatically polished version of your sentence."
]

GREAT_DICTION_MESSAGES = [
    "Fantastic work! Your pronunciation is spot on! 👌",
    "Brilliant! You nailed the pronunciation! 👍",
    "Outstanding! Your diction was perfect! 🌟"]

fernet_key = os.getenv("FERNET_KEY")

LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
XI_VOICE_IDS={'Rachel': '21m00Tcm4TlvDq8ikWAM', 'Domi': 'AZnzlk1XvdvUeBnXmlld', 'Antoni': 'ErXwobaYiN019PkySvjV'}
XI_LABS_API_KEY = os.getenv("XI_LABS_API_KEY")

SPEECHSUPER_APP_KEY = os.getenv("SPEECHSUPER_APP_KEY")
SPEECHSUPER_SECRET_KEY = os.getenv("SPEECHSUPER_SECRET_KEY")
pronunciation_types = {"English": "sent.eval", "Spanish": "sent.eval.sp", "Japanese": "sent.eval.jp", "German": "sent.eval.de", "French": "sent.eval.fr", "Mandarin Chinese": "sent.eval.cn"}

language_codes = {"English": "en", "Spanish": "es", "Japanese": "ja", "German": "de", "French": "fr", "Mandarin Chinese": "zh"} # ISO 639-1 format
flag_emoji = {"English": "🇺🇸", "Spanish": "🇪🇸", "Japanese": "🇯🇵", "German": "🇩🇪", "French": "🇫🇷", "Mandarin Chinese": "🇨🇳"}

voice_sample_language_codes = {"English": "en", "Spanish": "es", "Japanese": "jp", "German": "de", "French": "fr", "Mandarin Chinese": "cn"}
spacy_language_codes = {"English": "en_core_web_sm", "Spanish": "es_core_news_md", "Japanese": "ja_core_news_sm", "German": "de_core_news_sm", "French": "fr_core_news_md", "Mandarin Chinese": "zh_core_web_sm"}

voice_samples = {
    "English": { "Rachel":"rachel_en_intro.mp3", "Antoni": "antoni_en_intro.mp3", "Domi": "domi_en_intro.mp3"},
    "Spanish": { "Rachel": "rachel_es_intro.mp3", "Antoni": "antoni_es_intro.mp3", "Domi": "domi_es_intro.mp3"},
    "Japanese": { "Rachel": "rachel_jp_intro.mp3", "Antoni": "antoni_jp_intro.mp3", "Domi": "domi_jp_intro.mp3"},
    "German": { "Rachel": "rachel_de_intro.mp3", "Antoni": "antoni_de_intro.mp3", "Domi": "domi_de_intro.mp3"},
    "French": { "Rachel": "rachel_fr_intro.mp3", "Antoni": "antoni_fr_intro.mp3", "Domi": "domi_fr_intro.mp3"},
    "Mandarin Chinese": { "Rachel": "rachel_cn_intro.mp3", "Antoni": "antoni_cn_intro.mp3", "Domi": "domi_cn_intro.mp3"}
}

teacher_names = {
    "English": { "Rachel":"Rachel", "Antoni": "Antoni"},
    "Spanish": { "Rachel": "Raquel", "Antoni": "Antonio"},
    "Japanese": { "Rachel": "Reina", "Antoni": "Akira"},
    "German": { "Rachel": "Reinhilde", "Antoni": "Arnold"},
    "French": { "Rachel": "Roxane", "Antoni": "Antoine"},
    "Mandarin Chinese": { "Rachel": "Ran", "Antoni": "An-Shi"}
}

openai_voice_ids = {"Rachel": "alloy", "Antoni": "onyx"}

parts_of_speech = {
    'PROPN': 'proper noun',
    'NOUN': 'noun',
    'ADP': 'preposition',
    'SYM': 'symbol',
    'NUM': 'number',
    'VERB': 'verb',
    'ADV': 'adverb',
    'ADJ': 'adjective',
    'PRON': 'pronoun',
    'PUNCT': 'punctuation',
    'CCONJ': 'coordinating conjunction',
    'X': 'other',
    'INTJ': 'interjection',
    'SCONJ': 'subordinating conjunction',
    'AUX': 'auxiliary verb',
    'DET': 'determiner',
    'PART': 'particle'
}

color_code_POS = {
    'proper noun': '#1E90FF',  # Dodger Blue
    'noun': '#32CD32',  # Lime Green
    'preposition': '#FFD700',  # Gold
    'symbol': '#8A2BE2',  # Blue Violet
    'number': '#FF8C00',  # Dark Orange
    'verb': '#FF4500',  # Orange Red
    'adverb': '#6A5ACD',  # Slate Blue
    'adjective': '#20B2AA',  # Light Sea Green
    'pronoun': '#DA70D6',  # Orchid
    'punctuation': '#696969',  # Dim Gray
    'coordinating conjunction': '#00CED1',  # Dark Turquoise
    'other': '#808080',  # Gray
    'interjection': '#FF69B4',  # Hot Pink
    'subordinating conjunction': '#4682B4',  # Steel Blue
    'auxiliary verb': '#B22222',  # Firebrick
    'determiner': '#DAA520',  # Goldenrod
    'particle': '#2E8B57'  # Sea Green
}

SUBSCRIPTION_URL = "https://www.llanai.com/subscription"
TERMS_AND_CONDITIONS_URL = "https://www.llanai.com/tos"

STRIPE_PUBLISHABLE_KEY = os.getenv("STRIPE_PUBLISHABLE_KEY")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")

if ENV == "local":
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DB_URL = os.getenv("DB_URL")

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
TWILIO_API_KEY = os.getenv("TWILIO_API_KEY")
TWILIO_API_SECRET = os.getenv("TWILIO_API_SECRET")
TWILIO_API_URL = os.getenv("TWILIO_API_URL")    
KNOWN_HOST_URL = os.getenv('KNOWN_HOST_URL', 'https://your-default-host-url.com')

AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION_NAME = os.getenv("AWS_REGION_NAME")
AWS_CHAT_FOLDER = "chat_audios/"

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_URL = os.getenv("REDIS_URL")

BROKER_TYPE = os.getenv("BROKER_TYPE", "sqs")
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "sqs://")
QUEUE_NAME = os.getenv("QUEUE_NAME")
SQS_QUEUE_URL = os.environ.get('SQS_QUEUE_URL','')  

lesson_length = 20
chat_length = 10
pronounce_length = 10

BLOCK_LIST = ['+14075550100', '+18025550100']

ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")

OUTPUT_DIR = os.path.join(
    tempfile.gettempdir(),
    'output'
)

os.makedirs(OUTPUT_DIR, exist_ok=True)