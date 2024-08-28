# church-utils-backend

This repository is used as the backend service of [Church Utils](https://github.com/Pedro-Alonso/church-utils/) open source website.

It is built using Python 3 and run a Flask server.

## Run locally

In order to run this project locally, you must install the dependencies for that. To do so, you also must have Python 3 and Git installed on your machine.

If you have, complete the following steps:

- Open the Git Bash on the directory you'd like to clone the repository
- Clone this repo with `git clone https://github.com/Pedro-Alonso/church-utils-backend.git`
- Enter the cloned folder with `cd church-utils-backend`
- Run `./init_setup.sh` to setup the environment and install the dependencies

Once these are done, run the project locally with `flask run` (alternatively, `flask run --debug` for feedback logs on the terminal)

# API Documentation

## Base URL

The base local URL for all endpoints is: `http://127.0.0.1:8000`

The deployed URL is xxx

---

## Endpoints

### 1. Hello World

**Endpoint:** `/`

**Method:** `GET`

**Description:** This endpoint returns a simple "Hello, World!" message.

**Response:**

- **Status Code:** `200 OK`
- **Body:**
  ```json
  "<p>Hello, World!</p>"
  ```

**Example Request:**

```bash
curl -X GET http://127.0.0.1:5000/
```

**Example Response:**

```html
<p>Hello, World!</p>
```

---

### 2. Get Lyrics

**Endpoint:** `/get-lyrics/<string:artist>/<string:title>`

**Method:** `GET`

**Description:** This endpoint retrieves the lyrics of a song based on the artist and title provided in the URL path.

**Headers:**

- **Client-access-token:** `string` (required) - The Genius API access token.

**Path Parameters:**

- **artist:** `string` - The name of the artist.
- **title:** `string` - The title of the song.

**Responses:**

- **200 OK:** Returns the lyrics of the song.

  ```json
  {
    "lyrics": "string"
  }
  ```

- **400 Bad Request:** Returns an error if the `Client-access-token` header is missing.

  ```json
  {
    "error": "Client-access-token header is missing"
  }
  ```

- **404 Not Found:** Returns an error if the song is not found.
  ```json
  {
    "error": "Song not found"
  }
  ```

**Example Request:**

```bash
curl -X GET http://127.0.0.1:5000/get-lyrics/thalles-roberto/amor-maravilhoso \
  -H "Client-access-token: YOUR_ACCESS_TOKEN"
```

**Example Responses:**

- **200 OK:**

  ```json
  {
    "lyrics": "Filho, nunca te abandonei\nTe carreguei no colo tantas vezes..."
  }
  ```

- **400 Bad Request:**

  ```json
  {
    "error": "Client-access-token header is missing"
  }
  ```

- **404 Not Found:**
  ```json
  {
    "error": "Song not found"
  }
  ```
