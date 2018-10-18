package main

import (
		"crypto/tls"
    "fmt"
		"bytes"
    "io/ioutil"
    "net/http"
)

// Retrieving Authentication Token
func main() {
    url := "<Your_URL>"
    fmt.Println("URL:>", url)

    var jsonStr = []byte(`{"username": "<Username>", "password": "<Password>"}`)
    req, err := http.NewRequest("POST", url, bytes.NewBuffer(jsonStr))
    req.Header.Set("Content-Type", "application/json")
		tr := &http.Transport{
            TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
    }
    client := &http.Client{Transport: tr}
    resp, err := client.Do(req)
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()

    fmt.Println("response Status:", resp.Status)
    fmt.Println("response Headers:", resp.Header)
    body, _ := ioutil.ReadAll(resp.Body)
    fmt.Println("response Body:", string(body))
}
