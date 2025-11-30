import { useState } from "react";
import "./App.css";

function App() {
  const [email, setEmail] = useState("");
  const [preference, setPreference] = useState("");
  const [results, setResults] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();   // STOP PAGE REFRESH

    const res = await fetch("http://localhost:5000/recommend", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ preference }),
    });

    const data = await res.json();
    setResults(data.recommendations);
  };

  return (
    <div className="wrapper">
      <h1>Welcome</h1>
      <p className="subtitle">
        Discover your unique style with our personalized recommendations!
      </p>

      <form onSubmit={handleSubmit}>
        <div className="container1">
          <label htmlFor="email">Enter your gmail</label>
          <input
            type="email"
            id="email"
            name="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />

          <label htmlFor="cloth">Type your preference</label>
          <input
            type="text"
            id="cloth"
            name="cloth"
            value={preference}
            onChange={(e) => setPreference(e.target.value)}
          />

          <button type="submit">Submit</button>
        </div>
      </form>

      {results.length > 0 && (
        <div className="resultsBox">
          <h3>Your Recommendations</h3>

          {results.map((item, index) => (
            <div key={index} className="resultCard">
              <h4>{item.title}</h4>
              <p>{item.description}</p>
              <div className="tagRow">
                <span className="tag">{item.style}</span>
                <span className="tag">{item.color}</span>
                <span className="tag">{item.season}</span>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;
