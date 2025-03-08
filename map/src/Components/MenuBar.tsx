import "./MenuBar.css"; // Importing CSS for styling
import React, { useState } from "react";

const MenuBar: React.FC = () => {
  const [showPopup, setShowPopup] = useState(false);
  const [width, setWidth] = useState("");
  const [height, setHeight] = useState("");

  const handleNewMapClick = () => {
    setShowPopup(!showPopup);
  };

  const handleCreateMap = () => {
    const widthNum = parseInt(width, 10);
    const heightNum = parseInt(height, 10);

    if (!isNaN(widthNum) && !isNaN(heightNum)) {
      console.log(
        `Creating a new map with width: ${widthNum} and height: ${heightNum}`
      );
      setShowPopup(false);
    } else {
      alert("Please enter valid numeric values.");
    }
  };

  return (
    <div className="menu-bar">
      <button className="new-map-button" onClick={handleNewMapClick}>
        New Map
      </button>
      {showPopup && (
        <div className="popup">
          <label>
            Width:
            <input
              type="number"
              value={width}
              onChange={(e) => setWidth(e.target.value)}
            />
          </label>
          <label>
            Height:
            <input
              type="number"
              value={height}
              onChange={(e) => setHeight(e.target.value)}
            />
          </label>
          <button className="create-button" onClick={handleCreateMap}>
            Create
          </button>
          <button className="cancel-button" onClick={() => setShowPopup(false)}>
            Cancel
          </button>
        </div>
      )}
    </div>
  );
};

export default MenuBar;
