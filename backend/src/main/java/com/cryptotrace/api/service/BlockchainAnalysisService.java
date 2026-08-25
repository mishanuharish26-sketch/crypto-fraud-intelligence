package com.cryptotrace.api.service;

import org.springframework.stereotype.Service;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

@Service
public class BlockchainAnalysisService {

    private final HttpClient httpClient = HttpClient.newHttpClient();

    public String analyzeWallet(String walletAddress) {

        try {
            String jsonBody = """
                    {
                        "walletAddress": "%s"
                    }
                    """.formatted(walletAddress);

            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create("http://127.0.0.1:5000/analyze"))
                    .header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                    .build();

            HttpResponse<String> response =
                    httpClient.send(
                            request,
                            HttpResponse.BodyHandlers.ofString()
                    );

            if (response.statusCode() != 200) {
                return "Blockchain analysis failed. Python bridge returned HTTP "
                        + response.statusCode()
                        + ": "
                        + response.body();
            }

            return response.body();

        } catch (Exception e) {
            return "Blockchain analysis failed: " + e.getMessage();
        }
    }
}