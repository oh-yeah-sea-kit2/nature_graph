import remoclient
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


client = remoclient.NatureRemoClient()
events = client.get_newest_events()

print(events)
