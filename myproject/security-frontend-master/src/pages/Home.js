import React, { useState, useEffect } from "react";
import axios from "axios";
import "../styles/Home.css";

// myenv/bin/activate
// python manage.py runserver

function Home() {
  const [randomNumber, setRandomNumber] = useState(null);
  const [minValue, setMinValue] = useState(0);
  const [maxValue, setMaxValue] = useState(10);
  const [loading, setLoading] = useState(false);

  const handleGenerateRandom = () => {
    if (maxValue <= minValue) {
      alert("Maximum value must be greater than minimum value!");
      return;
    }

    setLoading(true);

    axios
      .get(`http://127.0.0.1:8000/api/random/${minValue}/${maxValue}/`)
      .then((response) => {
        setRandomNumber(response.data["random number"]);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error generating random number: ", error);
        setLoading(false);
      });
  };

  const handleMinChange = (event) => {
    setMinValue(parseInt(event.target.value));
  };

  const handleMaxChange = (event) => {
    setMaxValue(parseInt(event.target.value));
  };

  return (
    <div className="App">
      <h1>True Random Number Generator</h1>
      <div className="inputs">
        <div className="box">
          <label>Min: </label>
          <input type="number" value={minValue} onChange={handleMinChange} />
        </div>

        <div className="box">
          <label>Max: </label>
          <input type="number" value={maxValue} onChange={handleMaxChange} />
        </div>

        <button onClick={handleGenerateRandom}>Generate!</button>
        {loading ? (
          <p>Generating...</p>
        ) : randomNumber !== null ? (
          <p className="number">{randomNumber}</p>
        ) : (
          <p>Get a random number!</p>
        )}
      </div>
    </div>
  );
}

export default Home;
