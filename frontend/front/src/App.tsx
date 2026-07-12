import React from 'react'
import './App.css'
import { BrowserRouter, Link, Route, Routes } from "react-router-dom";
import Home from "./pages/Home/home";

function App() {
  
  return (
    <>
      <BrowserRouter>
        <nav>
          <Link to="/">Главная</Link> |{" "}
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
