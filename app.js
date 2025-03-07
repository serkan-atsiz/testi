import React, { useState } from'react';
import axios from 'axios';

function App() {
  const [text, setText] = useState('');
  const [result, setResult] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    const response = await axios.post('/api/analyze', { text });
    setResult(response.data);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="text" value={text} onChange={(event) => setText(event.target.value)} />
        <button type="submit">Analyze</button>
      </form>
      <p>{result}</p>
    </div>
  );
}

export default App;
