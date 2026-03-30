import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../services/api";

function Dashboard() {
  const [tasks, setTasks] = useState([]);
  const [editingId, setEditingId] = useState(null);
  const [form, setForm] = useState({
    title: "",
    description: "",
    status: "pending",
  });

  const navigate = useNavigate();
  const token = localStorage.getItem("token");

  const authHeaders = {
    authorization: `Bearer ${token}`,
  };

  const fetchTasks = async () => {
    try {
      const response = await API.get("/my-tasks", { headers: authHeaders });
      setTasks(response.data);
    } catch {
      alert("Failed to load tasks");
    }
  };

  useEffect(() => {
    if (!token) {
      navigate("/");
      return;
    }
    fetchTasks();
  }, []);

  const resetForm = () => {
    setForm({
      title: "",
      description: "",
      status: "pending",
    });
    setEditingId(null);
  };

  const handleSubmit = async () => {
    try {
      if (editingId) {
        await API.put(`/tasks/${editingId}`, form, { headers: authHeaders });
      } else {
        await API.post("/tasks/", form, { headers: authHeaders });
      }
      resetForm();
      fetchTasks();
    } catch (error) {
      alert(error.response?.data?.detail || "Operation failed");
    }
  };

  const handleEdit = (task) => {
    setEditingId(task.id);
    setForm({
      title: task.title,
      description: task.description || "",
      status: task.status,
    });
  };

  const handleDelete = async (id) => {
    try {
      await API.delete(`/tasks/${id}`, { headers: authHeaders });
      fetchTasks();
    } catch (error) {
      alert(error.response?.data?.detail || "Delete failed");
    }
  };

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  return (
    <div className="dashboard">
      <div className="dashboard-header">
        <div>
          <h1>My Tasks</h1>
          <p className="muted">Create, update, and manage your work.</p>
        </div>
        <button className="button secondary" onClick={handleLogout}>
          Logout
        </button>
      </div>

      <div className="panel">
        <h2>{editingId ? "Edit Task" : "Create Task"}</h2>

        <input
          className="input"
          placeholder="Task title"
          value={form.title}
          onChange={(e) => setForm({ ...form, title: e.target.value })}
        />

        <input
          className="input"
          placeholder="Task description"
          value={form.description}
          onChange={(e) => setForm({ ...form, description: e.target.value })}
        />

        <select
          className="select"
          value={form.status}
          onChange={(e) => setForm({ ...form, status: e.target.value })}
        >
          <option value="pending">pending</option>
          <option value="completed">completed</option>
        </select>

        <div className="row" style={{ marginTop: "12px" }}>
          <button className="button" onClick={handleSubmit}>
            {editingId ? "Update Task" : "Add Task"}
          </button>

          {editingId && (
            <button className="button secondary" onClick={resetForm}>
              Cancel
            </button>
          )}
        </div>
      </div>

      <div className="panel">
        <h2>Your Task List</h2>

        {tasks.length === 0 ? (
          <div className="empty">No tasks found</div>
        ) : (
          <div className="task-grid">
            {tasks.map((task) => (
              <div className="task-card" key={task.id}>
                <h3>{task.title}</h3>
                <p>{task.description || "No description"}</p>
                <span className={`badge ${task.status === "completed" ? "completed" : ""}`}>
                  {task.status}
                </span>

                <div className="actions">
                  <button className="button secondary" onClick={() => handleEdit(task)}>
                    Edit
                  </button>
                  <button className="button danger" onClick={() => handleDelete(task.id)}>
                    Delete
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default Dashboard;