# rse-api
Code for the RSE talk at PSI

Presentation for the talk: [link](./RSE%20talk.pdf).

## Installing and running the FastAPI server
1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/) - a modern package manager for Python. `uv` manages virtual environments, python installations, and dependencies, effectively replacing `pip` and `venv`.
2. `uv run fastapi dev` starts the development server at http://localhost:8000, with OpenAPI explorer at /docs
3. Open index.html in your browser for the Q&A website that talks to the above server

## Installing and running the Go server
1. Install the go toolchain >= v1.26.5
2. `cd go-server`. Then `go run main.go` starts the server at localhost:8090
3. To build a static binary: `CGO_ENABLED=0 go build -o rse-server` and then execute it `./rse-server`

To point the website at it, change `API_URL` in index.html to `http://localhost:8090`.

The Go server is only a sketch, not a replacement for the FastAPI one: `GET /questions` returns two hardcoded questions, other methods get a 501, and there is no upvote endpoint. So the questions will show up, but submitting and upvoting won't work.
