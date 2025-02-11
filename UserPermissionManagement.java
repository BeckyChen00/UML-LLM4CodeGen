import java.util.HashSet;
import java.util.Set;

// Member类代表用户
class Member {
    private String mid; // 用户ID
    private String name; // 用户名
    private Set<Role> roles; // 用户拥有的角色集合

    // 构造函数
    public Member(String mid, String name) {
        this.mid = mid;
        this.name = name;
        this.roles = new HashSet<>();
    }

    // 添加角色到用户
    public void setRoles(Role role) {
        roles.add(role);
    }

    // 获取用户的所有角色
    public Set<Role> getRoles() {
        return roles;
    }

    // 获取用户信息
    public String getInfo() {
        return "Member ID: " + mid + ", Name: " + name;
    }
}

// Role类代表角色
class Role {
    private long rid; // 角色ID
    private String title; // 角色名称
    private Set<Member> members; // 拥有此角色的用户集合
    private Set<Privilege> privileges; // 角色拥有的权限集合

    // 构造函数
    public Role(long rid, String title) {
        this.rid = rid;
        this.title = title;
        this.members = new HashSet<>();
        this.privileges = new HashSet<>();
    }

    // 添加用户到角色
    public void setMembers(Member member) {
        members.add(member);
    }

    // 获取角色的所有用户
    public Set<Member> getMembers() {
        return members;
    }

    // 添加权限到角色
    public void setPrivileges(Privilege privilege) {
        privileges.add(privilege);
    }

    // 获取角色的所有权限
    public Set<Privilege> getPrivileges() {
        return privileges;
    }

    // 获取角色信息
    public String getInfo() {
        return "Role ID: " + rid + ", Title: " + title;
    }
}

// Privilege类代表权限
class Privilege {
    private long pid; // 权限ID
    private String title; // 权限名称
    private Role role; // 权限所属的角色

    // 构造函数
    public Privilege(long pid, String title) {
        this.pid = pid;
        this.title = title;
    }

    // 设置权限所属的角色
    public void setRole(Role role) {
        this.role = role;
    }

    // 获取权限所属的角色
    public Role getRole() {
        return role;
    }

    // 获取权限信息
    public String getInfo() {
        return "Privilege ID: " + pid + ", Title: " + title;
    }
}

// 示例：如何使用这些类来构建用户权限管理系统的框架
public class UserPermissionManagement {
    public static void main(String[] args) {
        // 创建角色和权限
        Role adminRole = new Role(1, "Admin");
        Privilege manageUsers = new Privilege(1, "Manage Users");
        Privilege manageRoles = new Privilege(2, "Manage Roles");

        // 将权限分配给角色
        adminRole.setPrivileges(manageUsers);
        adminRole.setPrivileges(manageRoles);

        // 创建用户并将角色分配给用户
        Member user1 = new Member("U001", "Alice");
        user1.setRoles(adminRole);

        // 根据用户查询角色和权限
        for (Role role : user1.getRoles()) {
            System.out.println(role.getInfo());
            for (Privilege privilege : role.getPrivileges()) {
                System.out.println("  " + privilege.getInfo());
            }
        }
    }
}
