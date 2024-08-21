import Icon from "./icons";

const InputBase = (props) => {
  return (
    <>
      <label
        className={`input input-bordered flex items-center gap-2 ${props?.className} outline-none`}
        placeholder={props?.placeholder}>
        {props.children}
      </label>
    </>
  );
};

export const TextInput = (props) => {
  return (
    <InputBase>
      {props?.icon && <Icon icon={props?.icon} size="xs" className="pr-2" />}
      <input
        type={props?.type || "text"}
        className="w-full bg-none text-sm"
        placeholder={props?.placeholder}
        value={props?.value}
        onChange={props?.onChange}
        required={props?.required}
      />
    </InputBase>
  );
};

export const SelectInput = (props) => {
  return (
    <select className="select select-bordered w-full">
      <option disabled selected>
        Pick One
      </option>

      {props?.options?.map((option) => (
        <option key={option.value} value={option.value}>
          {option.name}
        </option>
      ))}
    </select>
  );
};
