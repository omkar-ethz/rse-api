package main

import (
	"encoding/json"
	"net/http"
)

type Question struct {
	Id      int    `json:"id"`
	Text    string `json:"text"`
	Upvotes int    `json:"upvotes"`
}

var questions = []Question{
	{1, "hello world from the go server", 0},
	{2, "hallo welt vom go server", 0},
}

func getQuestions(w http.ResponseWriter, req *http.Request) {
	// As it's a public API, allow cross origin requests
	w.Header().Set("Access-Control-Allow-Origin", "*")
	w.Header().Set("Access-Control-Allow-Methods", "*")
	w.Header().Set("Access-Control-Allow-Headers", "*")

	if req.Method == http.MethodOptions {
		return
	}

	if req.Method == http.MethodGet {
		q, err := json.Marshal(questions)
		if err != nil {
			w.WriteHeader(http.StatusInternalServerError)
			return
		}
		w.Header().Set("Content-Type", "application/json")
		w.Write(q)
	} else {
		w.WriteHeader(http.StatusNotImplemented)
	}
}

func main() {
	http.HandleFunc("/questions", getQuestions)

	http.ListenAndServe(":8090", nil)
}
