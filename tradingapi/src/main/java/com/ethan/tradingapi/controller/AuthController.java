package com.ethan.tradingapi.controller;

import com.ethan.tradingapi.model.User;
import com.ethan.tradingapi.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/auth")
public class AuthController {

    @Autowired
    private UserRepository userRepository;

    private BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder();

    @PostMapping("/register")
    public String register(@RequestBody User user) {
        if (userRepository.findByUsername(user.getUsername()).isPresent()) {
            return "Username already exists";
        }

        // Hash password
        user.setPassword(passwordEncoder.encode(user.getPassword()));

        // Save user
        userRepository.save(user);

        return "User registered successfully";
    }
}