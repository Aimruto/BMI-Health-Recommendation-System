import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Login from './components/Login';
import About from './components/About';
import HealthcareRecommendation from './components/HealthcareRecommendation';
import Calculator from './components/Calculator';
import Todo from './components/Todo';
import Footer from './components/Footer';
import Contact from './components/Contact';
import './App.css';

function App() {
  const [isLoginClicked, setIsLoginClicked] = useState(false);

  const handleLoginClick = () => {
    setIsLoginClicked(true);
  };

  const handleLogin = () => {
    // Your login logic goes here
    // For now, let's assume login is successful
    setIsLoginClicked(false); // Hide the login component after successful login
  };

  return (
    <Router>
      <div className="grid-container">
        <div className="grid-header">
          <Navbar onLoginClick={handleLoginClick} />
        </div>
        <div className='main-container'>
          <Routes>
            <Route path="/login" element={<div className="login"><Login onLogin={handleLogin} /></div>} />
            <Route path="/about" element={<div className="about"><About /></div>}></Route>
            <Route path="/contact" element={<div className="contact"><Contact /></div>}></Route>
            <Route path="/" element={<>
              <div className="healthcare-recommendation"><HealthcareRecommendation /></div>
              <div className="calculator"><Calculator /></div>
              <div className="todo"><Todo /></div>
              
            </>} />
          </Routes>
        </div>
        <div className="footer"><Footer /></div>
      </div>
    </Router>
  );
}

export default App;
