package com.cryptotrace.api.service;

import org.springframework.stereotype.Service;

@Service
public class BlockchainAnalysisService {

    public String analyzeWallet(String walletAddress) {
        return "Blockchain analysis queued for wallet: " + walletAddress;
    }
}