package com.cryptotrace.api.dto;

public class InvestigationResponse {

    private String investigationId;
    private String reportedAddress;
    private String chain;
    private String status;

    public InvestigationResponse() {
    }

    public InvestigationResponse(String investigationId,
                                  String reportedAddress,
                                  String chain,
                                  String status) {
        this.investigationId = investigationId;
        this.reportedAddress = reportedAddress;
        this.chain = chain;
        this.status = status;
    }

    public String getInvestigationId() {
        return investigationId;
    }

    public void setInvestigationId(String investigationId) {
        this.investigationId = investigationId;
    }

    public String getReportedAddress() {
        return reportedAddress;
    }

    public void setReportedAddress(String reportedAddress) {
        this.reportedAddress = reportedAddress;
    }

    public String getChain() {
        return chain;
    }

    public void setChain(String chain) {
        this.chain = chain;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
}