import React from 'react';
import { useNavigate } from 'react-router-dom';
import './SelectionPage.css';
import titleImage from '/Users/sairushitha/Downloads/Fake_Review_Monitoring_UI-main/frontend/review_frontend/src/assests/image4.png'; // Adjust the path as needed
import '/Users/sairushitha/Downloads/Fake_Review_Monitoring_UI-main/frontend/review_frontend/src/SelectionPage.css'; // Import the CSS file for styling

function SelectionPage() {
  const navigate = useNavigate();

  return (
    <div className="selection-container">
      <h1>
        <h3>FAKE PRODUCT REVIEW MONITORING SYSTEM</h3>
        <img src={titleImage} alt="Title" className="title-image" /> 
      </h1>
      <button className="styled-button" onClick={() => navigate('/review-login')}>
        CLICK HERE IF YOU WANT TO WRITE A REVIEW
      </button>
      <button className="styled-button" onClick={() => navigate('/login')}>
        CLICK HERE IF YOU WANT TO MAKE REVIEW ANALYSIS
      </button>
    </div>
  );
}

export default SelectionPage;
