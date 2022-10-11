import '../App.css';
import React, {useState} from 'react';

import {Link, Routes, Route, useNavigate} from 'react-router-dom';

function CreateAccount() {
  const [error, setError] = useState({});
  const [isSubmitted, setIsSubmitted] = useState(false);

  const navigate = useNavigate();

  const renderErrorMessage = (name) =>
    name === error.name && (
      <div className='error'>{error.message}</div>
    )

  const handleSubmit = (event) => {
    event.preventDefault();

    var { email, password } = document.forms[0]
    setIsSubmitted(true)
    navigate('/account/balance')
  }
  
  const renderForm = (
    <div className="form">
      <form onSubmit={handleSubmit}>
        <div className="input-container">
          <label>Email </label>
          <input type="text" name="email" required />
        </div>
        <div className="input-container">
          <label>Password </label>
          <input type="password" name="password" required />
          {renderErrorMessage("pass")}
        </div>
        <div className="button-container">
          <input type="submit" />
        </div>
      </form>
    </div>
  );

  return (
    <div className="App">
      <header className="App-header">
      <p>Welcome to Bambank</p>  
      <div className='login-form'>
        <div className='title'>Create Account:</div>
        {isSubmitted ? <div>Account Created</div> : renderForm}
      </div>
        <li>
        <Link to="/">Back</Link>
        </li>
      </header>
    </div>
  );
}

export default CreateAccount;
