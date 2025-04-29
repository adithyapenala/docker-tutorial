package com.DockerTutorial.SpringBackend.controller;

import com.DockerTutorial.SpringBackend.model.Train;
import com.DockerTutorial.SpringBackend.model.User;
import com.DockerTutorial.SpringBackend.service.TrainService;
import org.springframework.graphql.data.method.annotation.Argument;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.stereotype.Controller;

@Controller
public class UserController {


    @QueryMapping
    public String hello() {
        return "Hello, GraphQL!";
    }

    @QueryMapping
    public User userById(@Argument String id) {
        return new User(id, "John Doe", "john@example.com");
    }


}