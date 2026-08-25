package com.cryptotrace.api.controller;

import com.cryptotrace.api.dto.InvestigationRequest;
import com.cryptotrace.api.dto.InvestigationResponse;
import com.cryptotrace.api.model.Investigation;
import com.cryptotrace.api.repository.InvestigationRepository;
import com.cryptotrace.api.service.BlockchainAnalysisService;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.UUID;

@RestController
@RequestMapping("/api/v1/investigations")
public class InvestigationController {

    private final InvestigationRepository repository =
            new InvestigationRepository();

    private final BlockchainAnalysisService blockchainAnalysisService;

    public InvestigationController(
            BlockchainAnalysisService blockchainAnalysisService) {
        this.blockchainAnalysisService = blockchainAnalysisService;
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public InvestigationResponse createInvestigation(
            @RequestBody InvestigationRequest request) {

        String investigationId = "INV-" +
                UUID.randomUUID()
                        .toString()
                        .substring(0, 8)
                        .toUpperCase();

        Investigation investigation = new Investigation(
                investigationId,
                request.getWalletAddress(),
                request.getChain(),
                "CREATED"
        );

        repository.save(investigation);

        return new InvestigationResponse(
                investigation.getInvestigationId(),
                investigation.getReportedAddress(),
                investigation.getChain(),
                investigation.getStatus()
        );
    }

    @GetMapping("/{id}")
    public InvestigationResponse getInvestigation(
            @PathVariable String id) {

        Investigation investigation = repository.findById(id)
                .orElseThrow(() ->
                        new RuntimeException("Investigation not found"));

        return new InvestigationResponse(
                investigation.getInvestigationId(),
                investigation.getReportedAddress(),
                investigation.getChain(),
                investigation.getStatus()
        );
    }

    @PostMapping("/{id}/analyze")
    public String analyzeInvestigation(
            @PathVariable String id) {

        Investigation investigation = repository.findById(id)
                .orElseThrow(() ->
                        new RuntimeException("Investigation not found"));

        return blockchainAnalysisService.analyzeWallet(
                investigation.getReportedAddress()
        );
    }

    @GetMapping("/test")
    public String test() {
        return "CryptoTrace AI API is working!";
    }
}