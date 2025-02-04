import { useState } from "react";
import "./App.css";

function App() {
  const [count, setCount] = useState(1);
  const [text, setText] = useState("");

  return (
    <>
      <button onClick={() => setCount((count) => count + 1)}>
        count is {count}
      </button>

      <button onClick={() => setText((text) => text + "h")}>texto{text}</button>
    </>
  );
}

export default App;
