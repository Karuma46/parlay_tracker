import { useState } from "react";
import { SelectInput, TextInput } from "../../components/inputs";
import Modal from "../../components/modal";

const ParlayForm = ({ visible, hide }) => {
  const parlayOptions = [
    {
      name: "Home Win",
      value: 1,
    },
    {
      name: "Away Win",
      value: 2,
    },
    {
      name: "Home Loss",
      value: 3,
    },
    {
      name: "Away Loss",
      value: 4,
    },
    {
      name: "Draw",
      value: 5,
    },
  ];

  const [saving, setSaving] = useState(false);
  const [parlay, setParlay] = useState({
    name: "",
    description: "",
    outcome: 1,
    spread: 0,
  });

  const handleSubmit = () => {
    setSaving(false);
    api.parlay.post(parlay).then(() => hide());
  };

  return (
    <>
      <Modal
        visible={visible}
        hide={hide}
        modal_id="create-parlay"
        title="Create Parlay">
        <form className="flex flex-col gap-6" onSubmit={handleSubmit}>
          <TextInput
            placeholder="Name"
            value={parlay.name}
            onChange={(e) => setParlay({ ...parlay, name: e.target.value })}
            required
          />
          <TextInput
            placeholder="Description"
            value={parlay.description}
            onChange={(e) =>
              setParlay({ ...parlay, description: e.target.value })
            }
            required
          />
          <SelectInput
            placeholder="Outcome"
            options={parlayOptions}
            value={parlay.outcome}
            onChange={(e) => setParlay({ ...parlay, outcome: e.target.value })}
            required
          />
          <TextInput
            placeholder="Spread"
            type="number"
            value={parlay.spread}
            onChange={(e) => setParlay({ ...parlay, spread: e.target.value })}
          />
          <button className="btn">Create</button>
        </form>
      </Modal>
    </>
  );
};

export default ParlayForm;
