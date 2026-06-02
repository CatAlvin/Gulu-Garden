class TaskSystem:
    """Simple task system for Gulu Garden.

    Version 1.1 scope:
    - Load task definitions from data/tasks.json.
    - Track task progress.
    - Complete tasks automatically.
    - Give coin rewards once.
    """

    def __init__(self, task_data: dict) -> None:
        """Initialize task system with task configuration data."""
        self.task_data = task_data
        self.progress = self.create_default_progress()

    def create_default_progress(self) -> dict:
        """Create default progress data for all configured tasks."""
        progress = {}

        for task_id, task in self.task_data.items():
            progress[task_id] = {
                "status": "active",
                "progress": 0,
                "target": int(task.get("target_count", 1)),
                "reward_claimed": False,
            }

        return progress

    def load_progress(self, saved_progress: dict | None) -> None:
        """Load task progress from save data.

        Missing tasks will be filled with default progress.
        This keeps old saves compatible when new tasks are added.
        """
        default_progress = self.create_default_progress()

        if not isinstance(saved_progress, dict):
            self.progress = default_progress
            return

        for task_id, default_task_progress in default_progress.items():
            saved_task_progress = saved_progress.get(task_id)

            if not isinstance(saved_task_progress, dict):
                continue

            default_task_progress["status"] = saved_task_progress.get(
                "status",
                default_task_progress["status"],
            )
            default_task_progress["progress"] = int(
                saved_task_progress.get(
                    "progress",
                    default_task_progress["progress"],
                )
            )
            default_task_progress["target"] = int(
                saved_task_progress.get(
                    "target",
                    default_task_progress["target"],
                )
            )
            default_task_progress["reward_claimed"] = bool(
                saved_task_progress.get(
                    "reward_claimed",
                    default_task_progress["reward_claimed"],
                )
            )

        self.progress = default_progress

    def to_save_data(self) -> dict:
        """Return task progress data for saving."""
        return self.progress

    def handle_event(self, event_type: str, crop_id: str, player) -> list[str]:
        """Update tasks by event and give rewards.

        Args:
            event_type: For example, plant_crop or harvest_crop.
            crop_id: Crop id related to the event.
            player: Player object, used for adding coin rewards.

        Returns:
            A list of task completion messages.
        """
        completed_messages = []

        for task_id, task in self.task_data.items():
            task_progress = self.progress.get(task_id)

            if task_progress is None:
                continue

            if task_progress["reward_claimed"]:
                continue

            if task.get("event_type") != event_type:
                continue

            if task.get("target_crop_id") != crop_id:
                continue

            task_progress["progress"] += 1

            if task_progress["progress"] >= task_progress["target"]:
                task_progress["progress"] = task_progress["target"]
                task_progress["status"] = "completed"

                message = self.claim_reward(task_id, player)

                if message:
                    completed_messages.append(message)

        return completed_messages

    def claim_reward(self, task_id: str, player) -> str | None:
        """Claim reward for a completed task."""
        task = self.task_data.get(task_id)
        task_progress = self.progress.get(task_id)

        if task is None or task_progress is None:
            return None

        if task_progress["reward_claimed"]:
            return None

        if task_progress["status"] != "completed":
            return None

        reward = task.get("reward", {})
        reward_coins = int(reward.get("coins", 0))

        if reward_coins > 0:
            player.add_coins(reward_coins)

        task_progress["reward_claimed"] = True

        task_title = task.get("title_cn", task_id)

        return f"Task completed: {task_title}. +{reward_coins} coins."

    def get_task_summary_lines(self) -> list[str]:
        """Return short text lines for debugging or future HUD display."""
        lines = []

        for task_id, task in self.task_data.items():
            task_progress = self.progress.get(task_id, {})
            title = task.get("title_cn", task_id)
            current = task_progress.get("progress", 0)
            target = task_progress.get("target", task.get("target_count", 1))
            reward_claimed = task_progress.get("reward_claimed", False)

            if reward_claimed:
                status_text = "Done"
            else:
                status_text = f"{current}/{target}"

            lines.append(f"{title}: {status_text}")

        return lines