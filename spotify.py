import requests, base64, json
import csv

base_url = "https://api.spotify.com/v1"
token = "BQAGilEo_BHNCWKmBNh8kIiH57EZpUYgS1G5VaMky1RO6ez3TeJlkMbnwcZzUviN_0DS_Kv5Uf2uv85_Bzg"
headers = {'Authorization': 'Bearer ' + token}

# def get_song():

# def write_csv(data, file):


def write_data(data, file):
	# print(data)
	if len(data) > 0:
		fieldnames = list(data[0].keys())
		with open(file, 'w') as csvfile:
			writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
			writer.writeheader()
			writer.writerows(data)

def get_features(songs):
	url = base_url + '/audio-features'
	payload = {'ids': ','.join(songs)}
	# payload = json.dumps({"ids" : songs})
	# print(payload)
	# r =requests.post(url, headers=headers, data=payload)
	r =requests.get(url, headers=headers, params=payload)
	data = r.json()
	print(data)

	return data["audio_features"]
	# print(r.text)

def get_token():
	cred = "f12c70c647cb4268aa0df38b6ed6697d:4fe65b57bfda4304a55f226be1ad0bf0"
	byte =  cred.encode("utf-8")
	# b64Val = base64.b64encode(byte)
	b64 = base64.urlsafe_b64encode(cred.encode()).decode()
	auth = {'Authorization': 'Basic ' + b64}
	print(auth)
	payload = {"grant_type": "client_credentials"}
	response = requests.post("https://accounts.spotify.com/api/token", 
		data=payload, headers=auth)
	print(response.text)

def get_playlist_songs(playlist):
	url = base_url + "/playlists/" + playlist + "/tracks"
	r = requests.get(url, headers=headers)
	content = r.json()
	songs = content["items"]
	# print(songs[0])
	song_ids = list(map(lambda x: x["track"]["id"], songs))
	print(get_features(song_ids))
	# print(r.text)

get_token()
# get_features('4rMhnUBc5KjVa8oaj2mynQ')
#get_playlist_songs("37i9dQZEVXbLRQDuF5jeBp")