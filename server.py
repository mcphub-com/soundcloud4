import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/yuananf/api/soundcloud4'

mcp = FastMCP('soundcloud4')

@mcp.tool()
def song_info(track_url: Annotated[str, Field(description='')]) -> dict: 
    '''Get basic information of a song.'''
    url = 'https://soundcloud4.p.rapidapi.com/song/info'
    headers = {'x-rapidapi-host': 'soundcloud4.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'track_url': track_url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def song_download(track_url: Annotated[str, Field(description='')]) -> dict: 
    '''Download one song, the result is a url which you can get the song.'''
    url = 'https://soundcloud4.p.rapidapi.com/song/download'
    headers = {'x-rapidapi-host': 'soundcloud4.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'track_url': track_url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_info(profile_url: Annotated[str, Field(description='')]) -> dict: 
    '''Get basic user info'''
    url = 'https://soundcloud4.p.rapidapi.com/user/info'
    headers = {'x-rapidapi-host': 'soundcloud4.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'profile_url': profile_url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def playlist_info(playlist_url: Annotated[str, Field(description='')]) -> dict: 
    '''Get playlist info.'''
    url = 'https://soundcloud4.p.rapidapi.com/playlist/info'
    headers = {'x-rapidapi-host': 'soundcloud4.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'playlist_url': playlist_url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search(query: Annotated[str, Field(description='')],
           type: Annotated[str, Field(description='')]) -> dict: 
    '''Search the soundcloud, possible values for type are "track", "user", "playlist", "all".'''
    url = 'https://soundcloud4.p.rapidapi.com/search'
    headers = {'x-rapidapi-host': 'soundcloud4.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'type': type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
