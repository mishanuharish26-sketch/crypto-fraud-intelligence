package com.cryptotrace.api.dto;

public class InvestigationRequest {

    private String walletAddress;
    private String chain;

    public InvestigationRequest() {
    }

    public String getWalletAddress() {
        return walletAddress;
    }

    public void setWalletAddress(String walletAddress) {
        this.walletAddress = walletAddress;
    }

    public String getChain() {
        return chain;
    }

    public void setChain(String chain) {
        this.chain = chain;
    }
}