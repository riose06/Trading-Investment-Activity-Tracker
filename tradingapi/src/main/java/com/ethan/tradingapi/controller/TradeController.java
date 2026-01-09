package com.ethan.tradingapi.controller;

import com.ethan.tradingapi.model.Trade;
import com.ethan.tradingapi.model.User;
import com.ethan.tradingapi.repository.TradeRepository;
import com.ethan.tradingapi.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/trades")
public class TradeController {

    @Autowired
    private TradeRepository tradeRepository;

    @Autowired
    private UserRepository userRepository;

    // Add new trade
    @PostMapping
    public Trade addTrade(@AuthenticationPrincipal UserDetails userDetails, @RequestBody Trade trade) {
        User user = userRepository.findByUsername(userDetails.getUsername()).orElseThrow();
        trade.setUser(user);
        return tradeRepository.save(trade);
    }

    // List all trades for logged-in user
    @GetMapping
    public List<Trade> getTrades(@AuthenticationPrincipal UserDetails userDetails) {
        return tradeRepository.findByUserUsername(userDetails.getUsername());
    }

    // Get a single trade
    @GetMapping("/{id}")
    public Trade getTrade(@AuthenticationPrincipal UserDetails userDetails, @PathVariable Long id) {
        Trade trade = tradeRepository.findById(id).orElseThrow();
        if (!trade.getUser().getUsername().equals(userDetails.getUsername())) {
            throw new RuntimeException("Unauthorized");
        }
        return trade;
    }

    // Update a trade
    @PutMapping("/{id}")
    public Trade updateTrade(@AuthenticationPrincipal UserDetails userDetails,
                             @PathVariable Long id,
                             @RequestBody Trade updatedTrade) {
        Trade trade = tradeRepository.findById(id).orElseThrow();
        if (!trade.getUser().getUsername().equals(userDetails.getUsername())) {
            throw new RuntimeException("Unauthorized");
        }

        trade.setSymbol(updatedTrade.getSymbol());
        trade.setType(updatedTrade.getType());
        trade.setQuantity(updatedTrade.getQuantity());
        trade.setPrice(updatedTrade.getPrice());
        trade.setNotes(updatedTrade.getNotes());
        return tradeRepository.save(trade);
    }

    // Delete a trade
    @DeleteMapping("/{id}")
    public String deleteTrade(@AuthenticationPrincipal UserDetails userDetails, @PathVariable Long id) {
        Trade trade = tradeRepository.findById(id).orElseThrow();
        if (!trade.getUser().getUsername().equals(userDetails.getUsername())) {
            throw new RuntimeException("Unauthorized");
        }
        tradeRepository.delete(trade);
        return "Trade deleted successfully";
    }
}