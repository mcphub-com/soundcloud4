markdown
# Soundcloud4 MCP Server

## Overview

Soundcloud4 is a versatile MCP server designed to interact with Soundcloud's features. It allows users to download Soundcloud songs, search for users, tracks, or playlists, and retrieve detailed information about them. This server serves as a powerful tool for managing and interfacing with Soundcloud content efficiently.

## Features

- **Download Songs**: Retrieve a direct URL to download any song from Soundcloud using the provided track URL.
- **Search Functionality**: Perform searches across Soundcloud to find tracks, users, playlists, or all categories simultaneously.
- **User Information**: Obtain basic information about a Soundcloud user using their profile URL.
- **Playlist Information**: Access detailed information about a specific playlist using its URL.
- **Song Information**: Get basic details about a track using its URL.

## Tools and Functions

Soundcloud4 provides several tools to facilitate various operations:

- **/song/info**: 
  - Function: `song_info`
  - Description: Obtain basic information about a song.
  - Parameters: 
    - `track_url` (String, optional)

- **/song/download**:
  - Function: `song_download`
  - Description: Download a song, providing a URL to retrieve the song.
  - Parameters: 
    - `track_url` (String, optional)

- **/user/info**:
  - Function: `user_info`
  - Description: Retrieve basic user information.
  - Parameters:
    - `profile_url` (String, optional)

- **/playlist/info**:
  - Function: `playlist_info`
  - Description: Access playlist information.
  - Parameters:
    - `playlist_url` (String, optional)

- **/search**:
  - Function: `search`
  - Description: Search across Soundcloud for tracks, users, playlists, or all categories.
  - Parameters:
    - `query` (String, optional)
    - `type` (String, optional): Possible values are "track", "user", "playlist", or "all".

## Conclusion

Soundcloud4 MCP server simplifies the interaction with Soundcloud by providing robust tools for downloading and managing music content. Its features are tailored to enhance the user experience by allowing efficient content retrieval and management. Whether you need to download music, explore user profiles, or manage playlists, Soundcloud4 offers the necessary functionalities to streamline these processes.