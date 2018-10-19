package main

import (
    "io/ioutil"
    "log"
    "net/http"
		"crypto/tls"
)
// Retrieve Stat (Session Count)
func main() {
    url := "<Your_URL>"


    var bearer = "Bearer " + "<Your_Token>"

    req, err := http.NewRequest("POST", url, nil)


    req.Header.Add("Authorization", bearer)

    // Send req using http Client
		tr := &http.Transport{
            TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
    }
    client := &http.Client{Transport: tr}
    resp, err := client.Do(req)
    if err != nil {
        log.Println("Error on response.\n[ERRO] -", err)
    }

    body, _ := ioutil.ReadAll(resp.Body)
    log.Println(string([]byte(body)))
}
