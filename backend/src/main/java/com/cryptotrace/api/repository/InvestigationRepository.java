package com.cryptotrace.api.repository;

import com.cryptotrace.api.model.Investigation;

import java.util.Map;
import java.util.Optional;
import java.util.concurrent.ConcurrentHashMap;

public class InvestigationRepository {

    private final Map<String, Investigation> investigations =
            new ConcurrentHashMap<>();

    public Investigation save(Investigation investigation) {
        investigations.put(
                investigation.getInvestigationId(),
                investigation
        );
        return investigation;
    }

    public Optional<Investigation> findById(String investigationId) {
        return Optional.ofNullable(investigations.get(investigationId));
    }
}