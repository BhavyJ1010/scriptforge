Point:     x, y, t_relative

Stroke:    id, list of Points

Recording: id, prompt_id, list of Strokes, device_type, input_method,
           recording_start_time, canvas_width, canvas_height
           (only the accepted attempt is saved — rejects discarded by default)

Prompt:    id, version, text, category

Session:   id, writer_id, timestamp, list of Recording ids

Writer:    id, list of Session ids