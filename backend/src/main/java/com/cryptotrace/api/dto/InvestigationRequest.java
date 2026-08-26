package com.cryptotrace.api.dto;

import jakarta.validation.constraints.NotBlank;

public class InvestigationRequest {

    @NotBlank(message = "Wallet address is required")
    private String walletAddress;

    @NotBlank(message = "Blockchain chain is required")
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