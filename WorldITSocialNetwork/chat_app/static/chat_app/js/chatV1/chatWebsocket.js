let chatSocket
export let lastChatId

document.addEventListener("ws:openChat", (e) => {
    const { chatId } = e.detail

    if (lastChatId === chatId) {
        return
    }

    lastChatId = chatId

    if (chatSocket) {
        chatSocket.close()
    }

    chatSocket = new WebSocket(`ws://${WebsocketBackendURL}/chat/${chatId}/`)
    chatSocket.onmessage = (e) => recieveMessage(e)
})

function recieveMessage(event) {
    const data = JSON.parse(event.data)

    switch (data.type) {
        case "handshake":
            document.dispatchEvent(new CustomEvent("dom:openChat", {
                detail: {
                    chatId: data.chat_id,
                    chatName: data.chat_name,
                    chatAvatarUrl: data.chat_avatar_url
                }
            }))
            break;
        case "send_message":
            document.dispatchEvent(new CustomEvent("dom:insertMessage", {
                detail: {
                    html: data.html
                }
            }))
            break;
    }
}

/**
import { IChat } from "@modules/chats/api/api.types";
import { socket } from "@shared/socket/socket";
import { getAvatar } from "@shared/utils/avatar";
import { getOtherUser } from "@shared/utils/friends";
import { useRouter } from "expo-router";
import { TouchableOpacity, Image, View, Text } from "react-native";
import { styles } from "./styles";
import { COLORS } from "@shared/constants/colors";
import { SmallUserCard } from "@shared/ui/smallUserCard/SmallUserCard";

export function PersonalChatFrame(props: {chat: IChat, unreadCount?: number, chatUnreadCount?: number, isGroupChat?: boolean}){
    const { chat, unreadCount, chatUnreadCount, isGroupChat } = props
    const router = useRouter()
    const participantUser = chat.chat_app_chat_users[0]?.user_app_user
    return (
        <TouchableOpacity
            style={[{ flexDirection: "row", gap: 12 }]}
            onPress={() => {
                socket.emit("joinChat", {
                    chatId: chat.id,
                });
                router.push(`(chats)/${chat.id}?count=${unreadCount}&${chat.is_group === true ? `is_group=${chat.is_group}` : undefined}`);
            }}
        >
            <SmallUserCard 
                pseudonym={isGroupChat ? chat.name : participantUser.profile_app_profile.pseudonym} 
                avatar={isGroupChat ? chat.avatar : participantUser.profile_app_profile.avatar} 
                isGroup={isGroupChat}
                groupName={chat.name}
                lastMessage={
                    chat.chat_app_message &&
                    chat.chat_app_message.length !== 0
                        ? chat.chat_app_message[0].text
                        : undefined
                    }
                time={
                    chat.chat_app_message &&
                    chat.chat_app_message.length !== 0
                        ? chat.chat_app_message[0].created_at
                        : undefined
                    }
                unreadCount={chatUnreadCount}
                />
        </TouchableOpacity>
    )
}
 */