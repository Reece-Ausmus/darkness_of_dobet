import "./MenuBar.css";
import React, { useState } from "react";

type MenuBarProps = {
  setMap: React.Dispatch<React.SetStateAction<number[][][]>>;
};

const MenuBar: React.FC<MenuBarProps> = ({ setMap }) => {
  const [showPopup, setShowPopup] = useState(false);
  const [width, setWidth] = useState("");
  const [height, setHeight] = useState("");

  const handleNewMapClick = () => {
    setShowPopup(!showPopup);
  };

  const handleOpenMapClick = () => {
    const fileInput = document.createElement("input");
    fileInput.type = "file";
    fileInput.accept = ".json";

    fileInput.onchange = (event: any) => {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
          const content = e.target?.result;
          try {
            // Parse the content from the file
            const data = JSON.parse(content as string);

            // Check if the map is in the correct structure
            if (Array.isArray(data?.map)) {
              // Set the map state
              setMap(data.map);
              console.log("Map loaded successfully:", data.map);
            } else {
              console.error("Invalid map structure");
            }
          } catch (error) {
            console.error("Error reading or parsing the file", error);
          }
        };
        reader.readAsText(file);
      }
    };

    fileInput.click();
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
      <button className="open-map-button" onClick={handleOpenMapClick}>
        Open Map
      </button>
    </div>
  );
};

export default MenuBar;
