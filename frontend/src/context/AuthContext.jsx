// frontend/src/context/AuthContext.js
import React, { createContext, useState, useContext } from "react";
import apiClient from "../api";

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  // We'll store the token in state. We also check localStorage for an existing token.
  const [token, setToken] = useState(localStorage.getItem("authToken"));

  const login = async (username, password) => {
    const response = await apiClient.post("/users/token/", {
      username,
      password,
    });
    const newToken = response.data.access;
    setToken(newToken);
    localStorage.setItem("authToken", newToken);
  };

  const logout = () => {
    setToken(null);
    localStorage.removeItem("authToken");
  };

  const authValue = {
    token,
    login,
    logout,
  };

  return (
    <AuthContext.Provider value={authValue}>{children}</AuthContext.Provider>
  );
};

// A custom hook to easily access the auth context
export const useAuth = () => {
  return useContext(AuthContext);
};
