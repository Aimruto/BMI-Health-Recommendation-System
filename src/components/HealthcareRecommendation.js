import React from 'react';
import "./healthcarerecommendation.css";
const HealthcareRecommendation = () => {
  const handleClick = () => {
    window.open('http://localhost:8501/', '_blank');
  };

  return (
    <div className="recommendation-container">
      <h2 className='health-head'>To get personal healthcare recommendation, click the button below:</h2>
      <button className="recommendation-button" onClick={handleClick}>Get Recommendation</button>
    </div>
  );
};

export default HealthcareRecommendation;
